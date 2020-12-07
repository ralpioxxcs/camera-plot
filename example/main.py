import plot
import file

def main():
    model, ext = file.read('.')
    plot.show_extrinsic(model, ext)

if __name__ == "__main__":
	main()
