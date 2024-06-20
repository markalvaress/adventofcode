import re

codes_file = open("input.txt", "r")
codes = codes_file.read()
codes_file.close()

codes_list = codes.split("\n")

# pt 1 -----------------------------
# Since the digits are strings, this + is a string concatenation, not addition of integers
def get_calibration_vals(codes_list):
    digits_list = [re.findall("\d", code) for code in codes_list]
    calibration_vals_str = [digits[0] + digits[len(digits) - 1] for digits in digits_list[:-1]] # doing up to -1 because the last line is empty
    calibration_vals = [int(cv_str) for cv_str in calibration_vals_str]
    return calibration_vals

calibration_vals = get_calibration_vals(codes_list)

calib_vals_sum = sum(calibration_vals)

# pt 2 ----------------------------
# Now we want to also match those digits that are written out as chars
str_to_digits = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                 "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# This contains matches from above so we want to check against this dictionary first
str_to_digits_superset = {"twone": "21", "oneight": "18", "threeight": "38", "fiveight": "58",
                          "nineight": "98", "sevenine": "79", "eightwo": "82", "eighthree": "83"} # digits crossed this covers all bases

def replace_string_digits(str_w_digits, str_to_digits_dict, str_to_digits_superdict):
    str_dig_replace = str_w_digits
    for digit_str in str_to_digits_superdict:
        str_dig_replace = re.sub(digit_str, str_to_digits_superdict[digit_str], str_dig_replace)

    for digit_str in str_to_digits_dict:
        str_dig_replace = re.sub(digit_str, str_to_digits_dict[digit_str], str_dig_replace)

    return str_dig_replace

codes_list_inc_chars = [replace_string_digits(code, str_to_digits, str_to_digits_superset) for code in codes_list]

calib_vals_w_str = get_calibration_vals(codes_list_inc_chars)

calib_vals_w_str_sum = sum(calib_vals_w_str)
