import os, sys, unittest, binascii
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy
import array, time, math, numpy

class SHAgpu:

    cuda_inited = False
    
    threadMax = 1024
    blockMax = 1024
    cuda_buf_size =  threadMax

    def __init__(self, threadMax = 1024, blockMax = 1024):
        self.threadMax = threadMax
        self.blockMax = blockMax

    def init_cuda(self):
        if self.cuda_inited:
            return

        f = open('sha1.c')
        cuda_kernel = f.read()
        f.close()
        self.mod = SourceModule(cuda_kernel)

        self.cuda_buf = cuda.mem_alloc(self.cuda_buf_size)

        self.cuda_inited = True

    def cuda_run(self):
        self.init_cuda()

        run = self.mod.get_function("run");
        for threadNum in xrange(0, 1024*512):
            run(self.cuda_buf, block = (threadNum % 1024 + 1, 1, 1), grid = (1, 1))



class TestSHAgpu(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_benchmark(self):

        hasher = SHAgpu()
        hasher.cuda_run()


if __name__ == "__main__":
    unittest.main()
