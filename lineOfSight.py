# Given 2d positions pos1 and pos2, tuples, check straight line connected or not
# returns true if line of sight connected
# blocked = list of blocked positions
def line_of_sight(pos1, pos2, blocked):
    x0, y0 = pos1
    x1, y1 = pos2
    f = 0
    dx = x1 - x0
    dy = y1 - y0
    sy = 1
    sx = 1
    if dy < 0:
        dy = -dy
        sy = -1
    if dx < 0:
        dx = -dx
        sx = -1
    if dx >= dy:
        while x0 != x1:
            f = f + dy
            if f >= dx:
                if (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                    return False
                y0 = y0 + sy
                f = f - dx
            if f != 0 and (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                return False
            if dy == 0 and (x0 + (sx-1)/2, y0) in blocked and (x0 + (sx-1)/2, y0 - 1) in blocked:
                return False
            x0 = x0 + sx
    else:
        while y0 != y1:
            f = f + dx
            if f > dy:
                if (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                    return False
                x0 = x0+sx
                f = f-dy
            if f != 0 and (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                return False
            if dx == 0 and (x0, y0 + (sy-1)/2) in blocked and (x0 - 1, y0 + (sy-1)/2) in blocked:
                return False
            y0 = y0 + sy
    return True