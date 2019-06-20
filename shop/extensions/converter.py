########################################################################################################
#-----------------------------------code execution-----------------------------------------------------#
########################################################################################################
# for transmition in to <yyyy:year>
class fourDigitYearConverter:
    # define regex
    regex = "[0-9]{4}"
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return "%04d" % value