#!/usr/bin/env python3

import os, sys, numpy, csv

os.chdir(sys.argv[1])

benchmarks = [ 'gcbd', 'revolution', 'sample', 'urbanek' ]

results = {}
for benchmark in benchmarks:
  results[benchmark] = {}


for root, dirs, files in os.walk('.'):
   for name in files:
     if name == 'nohup.out':
       machine_type = root.split(os.sep)[-1]

       with open(root+os.sep+name,'r') as output_file:
        run = 1
        benchmark_idx = 0
        for line in output_file:
          if 'real' in line:
            m, s = line.split()[-1].split('m')
            s = float(m)*60 + float(s.rstrip('s'))
            try:
              results[benchmarks[benchmark_idx % 4]][machine_type].append(s)
            except KeyError:
              results[benchmarks[benchmark_idx % 4]][machine_type] = [s]
            benchmark_idx += 1

with open('results.csv', 'w') as results_file:
  results_writer = csv.writer(results_file, delimiter=',')
  results_writer.writerow(['']+list(results[benchmarks[0]]))
  for benchmark in benchmarks:
    row = []
    row.append(benchmark)
    for machine_type in results[benchmark]:
      mean = "{0:.3f}".format(numpy.mean(results[benchmark][machine_type]))
      std = "{0:.3g}".format(numpy.std(results[benchmark][machine_type]))
      row.append(str(mean) + '±' + str(std))
    results_writer.writerow(row)

  




