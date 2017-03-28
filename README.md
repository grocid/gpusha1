# gpusha1

A simplistic implementation of a CUDA-enhanced proof-of-work solver written in C and pycuda. Compared with a multithreaded Python implementation
which achieves around 1.7 MH/s running on 12 threads (5820k @ 3.6 GHz), the CUDA implementation runs with a hashrate of 138 MH/s (NVidia GeForce GTX 760).

