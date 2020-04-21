import zlib
import gzip
import vcf
import allel
import pandas as pd

reader = vcf.Reader(open('clinvar.vcf.gz', 'r'))

with open('clinvar.vcf.gz', mode='r', encoding='ascii') as vcf:
    print(vcf.read())

with open('clinvar.vcf.gz', mode='r', encoding='ascii') as vcf:
    gzip_vcf = gzip.GzipFile(fileobj=vcf)
    cvp = pd.read_csv(gzip_vcf)

f = gzip.open('clinvar.vcf.gz', 'rb')
file_content = f.read()
f.close()

with open(file_content, mode='r') as vcf:
    cvp = pd.read_csv(gzip_vcf)

print(1)