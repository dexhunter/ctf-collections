import gmpy2
from multiprocessing import Pool
pool = Pool(4)

n = 0x6270470b5e45bb464233683c38eeb03d17d54e0127038c9d286b00ac54946cfa1aa05c33610ec439c449b31f705c9e470ab6443cd090f9d88fab68f016c41bc00b9a1def40e77d836252ff03db2a525742e49b824d375216370d1cd810a60e2eac1824f306205c144b54c5f010ae17c8c88e76d1b41f13313cbd7e1b37822a0d

c = 431396049519259356426983102577521801906916650819409770125821662319298730692378063287943809162107163618549043548748362517694341497565980142708852098826686158246523270988062866178454564393347346790109724455155942667492571325721344535616869

def calc(j):
    # print j
    a, b = gmpy2.iroot(c + j * n, 3)
    if b == 1:
        m = a
        print '{:x}'.format(int(m)).decode('hex')
        pool.terminate()
        exit()

def SmallE():
    inputs = range(0, 130000000)
    pool.map(calc, inputs)
    pool.close()
    pool.join()



if __name__ == '__main__':
    print 'start'
    # SmallE()
    import gmpy
    m = gmpy.root(c, 3)[0]
    print(m)
    print(pow(m, 3, n) == c)
    from Crypto.Util.number import long_to_bytes
    print(long_to_bytes(m))

