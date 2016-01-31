import csv
import preppy
import sys

from rlextra.rml2pdf import rml2pdf

def main():
	data = "names.csv"

	with open(data) as a:
		reader = csv.reader(a)
		template = preppy.getModule("ex14.prep")

		for row in reader:
			name = row[0]
			location = row[1]

			rmltext = template.get(name,location)

			pdfFileName = name + ".pdf"
			rml2pdf.go(rmltext,outputFileName=pdfFileName)

			print("Guardado {}".format(pdfFileName))
	
	a.close()
	

if __name__ == '__main__':
	main()