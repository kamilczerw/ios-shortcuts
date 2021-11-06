import sys
import re

def validate_args(date, hours):
  if not re.match(r"^[0-9]{4}-((0[1-9])|(1[0-2]))-(([0-2][0-9])|(3[01]))$", date):
    print("Wrong date format, correct format: YYYY-MM-dd (e.g. 2021-11-05)")
    sys.exit(1)

  if not re.match(r"^(([0-1][0-9])|(2[0-4])):[0-5][0-9]$", hours):
    print("Wrong hours format, correct format: HH:mm (e.g. 08:00)")
    sys.exit(1)

  return date, hours

# def main():
#   date, hours = parse_args()
  

# if __name__ == '__main__':
#   main()
