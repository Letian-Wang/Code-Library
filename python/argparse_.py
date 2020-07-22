""" https://docs.python.org/zh-cn/3/howto/argparse.html """
import argparse
""" Basic """
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# parser.add_argument("square", help="display a square of a given number", type = int)
# args = parser.parse_args()
# print(args.echo)
# print(args.square**2)
# python argparse.py
# python argparse.py -h
# python argparse.py --help
# python argparse.py 1 2

""" optional and short command """
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbose", action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbose turned on")

# python argparse.py
# python argparse.py --verbose
# python argparse.py -v
# python argparse.py --verbose 1

''' Mixed with bool '''
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a sqaure of a given number")
# parser.add_argument("-v", "--verbose", action="store_true", help="increase outpu verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(" The square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)

# python argparse.py
# python argparse.py 2
# python argparse.py 2 --verbose
# python argparse.py --verbose 2

''' Mixed with choices '''
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("The square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)

# python argparse.py
# python argparse.py 1
# python argparse.py 1 -v 0
# python argparse.py -v 0 1


''' Mixed, default, count '''
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display the square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0, help ="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)

# python argparse.py 4
# python argparse.py 4 -v
# python argparse.py 4 -vv

''' more argument '''
# parser = argparse.ArgumentParser()
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbosity >= 2:
#     print("Running '{}'".format(__file__))
# if args.verbosity >= 1:
#     print("{}^{} == ".format(args.x, args.y), end="")
# print(answer)

# python argparse.py 2 4
# python argparse.py 2 4 -v
# python argparse.py 2 4 -vv

''' conflict and description '''
# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y

# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# else:
#     print("{}^{} == {}".format(args.x, args.y, answer))

# python argparse.py -h
# python argparse.py 2 4 -q
# python argparse.py 2 4 -v