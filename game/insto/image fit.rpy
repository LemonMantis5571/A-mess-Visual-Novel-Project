init python:
    def get_image_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h
    def image_fit(im, sz, f=0):
        im = get_image_size(im)
        if im[0] < sz[0] and im[1] < sz[1] and f:
            r = 1
        else:
            xr = float(sz[0])/float(im[0])
            yr = float(sz[1])/float(im[1])
            if yr*im[0] > sz[0]:
                r = xr
            else:
                r = yr
        return r

transform fit_zoom(z):
    zoom z