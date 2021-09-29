from fracoes import Fracoes
import sys

def main(argv=None):
		f = "fracao.txt"
		if argv is None:
			argv = sys.argv

		if(len(argv) > 1):
			f = argv[1]

		try:
			m = Fracoes(f)
			print(repr(m))
			print(m)
		except IOError:
			sys.exit("File %s not found." %f)

if __name__=="__main__":
	sys.exit(main())

