import re
import simplejson

from metapolator.metapost import Metapost
from metapolator.models import GlyphParam, GlyphOutline, Glyph, LocalParam


def get_edges_json(log_filename, glyphid=None, master=None):
    try:
        fp = open(log_filename)
        content = fp.read()
        fp.close()
        return get_json(content, glyphid=glyphid, master=master)
    except (IOError, OSError):
        pass
    return []


def get_edges_json_from_db(master, glyphid):
    glyph = Glyph.get(master_id=master.id, name=glyphid)

    points = GlyphOutline.filter(glyph_id=glyph.id)
    localparam = LocalParam.get(id=master.idlocala)

    _points = []
    for point in points.order_by(GlyphOutline.pointnr.asc()):
        param = GlyphParam.get(glyphoutline_id=point.id)
        iszpoint = False
        if re.match('z(\d+)[lr]', param.pointname):
            iszpoint = True

        x = point.x
        if localparam:
            x += localparam.px

        params = param.as_dict()
        params.update({'width': glyph.width})
        params.update({'width_new': glyph.width_new})
        _points.append({'x': x, 'y': point.y, 'pointnr': point.pointnr,
                        'iszpoint': iszpoint, 'data': params})

    return {'width': glyph.width, 'points': _points}


def get_json(content, glyphid=None, master=None):
    contour_pattern = re.compile(r'Filled\scontour\s:\n(.*?)..cycle',
                                 re.I | re.S | re.M)
    point_pattern = re.compile(r'\(([-\d.]+),([-\d.]+)\)..controls\s'
                               r'\(([-\d.]+),([-\d.]+)\)\sand\s'
                               r'\(([-\d.]+),([-\d.]+)\)')

    pattern = re.findall(r'\[(\d+)\]\s+Edge structure(.*?)End edge', content,
                         re.I | re.DOTALL | re.M)
    glyphs = []
    for glyph, edge in pattern:
        if glyphid and int(glyphid) != int(glyph):
            continue

        x_min = 0
        y_min = 0
        x_max = 0
        y_max = 0

        contours = []

        zpoints_names = []
        if master:
            glyph_obj = Glyph.get(master_id=master.id, name=glyph)
            zpoints_names = map(lambda x: x.pointname,
                                glyph_obj.get_zpoints())

        number = 0
        for ix, contour in enumerate(contour_pattern.findall(edge.strip())):
            contour = re.sub('\n(\S)', '\\1', contour)
            _contours = []
            handleIn_X, handleIn_Y = None, None

            for point in contour.split('\n'):
                point = point.strip().strip('..')
                match = point_pattern.match(point)
                if not match:
                    continue

                X = match.group(1)
                Y = match.group(2)

                handleOut_X = match.group(3)
                handleOut_Y = match.group(4)

                controlpoints = [{'x': 0, 'y': 0},
                                 {'x': handleOut_X, 'y': handleOut_Y}]
                if handleIn_X is not None and handleIn_Y is not None:
                    controlpoints[0] = {'x': handleIn_X, 'y': handleIn_Y}

                pointdict = {'x': X, 'y': Y, 'controls': controlpoints}
                _contours.append(pointdict)

                handleIn_X = match.group(5)
                handleIn_Y = match.group(6)

                x_min = min(x_min, x_max, float(X),
                            float(handleOut_X), float(handleIn_X))
                y_min = min(y_min, y_max, float(Y),
                            float(handleOut_Y), float(handleIn_Y))
                x_max = max(x_max, x_min, float(X),
                            float(handleOut_X), float(handleIn_X))
                y_max = max(y_max, y_min, float(Y),
                            float(handleOut_Y), float(handleIn_Y))

            if zpoints_names:
                zpoints = []
                ll = zpoints_names[number + 1: len(_contours) + number]
                if len(zpoints_names) > number:
                    zpoints = [zpoints_names[number]] + ll

                number += len(_contours)

                for zix, point in enumerate(_contours):
                    try:
                        point['pointname'] = zpoints[zix]
                    except IndexError:
                        pass

            if handleIn_X and handleIn_Y:
                _contours[0]['controls'][0] = {'x': handleIn_X,
                                               'y': handleIn_Y}

            contours.append(_contours)

        zpoints = []
        if master:
            zpoints = get_edges_json_from_db(master, glyph)

            g = Glyph.get(master_id=master.id, name=glyph)
            maxx, minx = GlyphOutline.minmax(GlyphOutline.x, glyph_id=g.id)[0]
            maxy, miny = GlyphOutline.minmax(GlyphOutline.y, glyph_id=g.id)[0]

            if maxx is not None and minx is not None \
                    and maxy is not None and miny is not None:
                x_min = min(x_min, minx, x_max, maxx)
                x_max = max(x_min, minx, x_max, maxx)
                y_min = min(y_max, maxy, y_min, miny)
                y_max = max(y_max, maxy, y_min, miny)

        if x_min < 0:
            width = abs(x_max) + abs(x_min)
        else:
            width = abs(x_max)

        if y_min < 0:
            height = abs(y_max) + abs(y_min)
        else:
            height = abs(y_max)

        json = {'name': glyph, 'contours': contours, 'minx': x_min,
                'miny': y_min, 'zpoints': zpoints, 'width': width,
                'height': height}

        if master and glyph_obj and not glyph_obj.original_glyph_contours:
            glyph_obj.original_glyph_contours = simplejson.dumps(contours)

        glyphs.append(json)

    return glyphs


def get_glyphs_jsondata(glyphid, master):
    project = master.project
    masters = project.get_ordered_masters()

    glyph = Glyph.get(master_id=master.id, name=glyphid)

    metapost = Metapost(project)
    metapost.execute_interpolated_single(glyph)

    instancelog = project.get_instancelog(masters[0].version)
    M_glyphjson = get_edges_json(instancelog, glyphid)

    metapost.execute_single(master, glyph)
    instancelog = project.get_instancelog(master.version, 'a')
    glyphjson = get_edges_json(instancelog, glyphid, master)

    return {'M': M_glyphjson, 'R': glyphjson, 'master_id': master.id}