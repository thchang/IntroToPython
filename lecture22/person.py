class Person():
    """ Define the Person class, describing a person by their name and DOB.

    Contains the following methods:

    __init__(self, name="NA NA", DOB="0/0/0") -- constructor

    __str__(self): returns str

    setName(self, name)

    setDOB(self, DOB)

    getName(self): returns str

    getDOB(self): returns str

    canVote(self): returns bool

    """

    def __init__(self, name="NA NA", DOB="0/0/0"):
        """ Constructor for Person class.

        Args:
            name (str): The person's name in 'First Last' format. Must
                contain exactly 2 names, separated by a space

            DOB (str): The person's DOB in MM/DD/YYYY format

        """

        # split names and DOB
        names = name.split()
        monthDayYear = DOB.split("/")
        # check length of names/monthDayYear lists
        if len(names) != 2:
            raise ValueError("name must have form 'First Last', separated "
                             "by a space")
        if len(monthDayYear) != 3:
            raise ValueError("Please enter DOB in MM/DD/YYYY format")
        # assign first/last names
        self.firstName = str(names[0])
        self.lastName = str(names[1])
        # try to assign birth month/day/year
        try:
            self.birthMonth = int(monthDayYear[0])
            self.birthDay = int(monthDayYear[1])
            self.birthYear = int(monthDayYear[2])
        except ValueError:
            raise ValueError("Could not parse DOB. Make sure it is given in "
                             "MM/DD/YYYY format, where MM, DD, and YYYY are "
                             "all integers")
        return

    def __str__(self):
        """ Convert Person object into a string output.

        Returns:
            str: Person's name and DOB in string format

        """

        return str(f"{self.firstName} {self.lastName}: "
                   f"{self.birthMonth}/{self.birthDay}/{self.birthYear}")

    def setName(self, name):
        """ Change the name of a Person.

        Args:
            name (str): The person's name in 'First Last' format. Must
                contain exactly 2 names, separated by a space

        """

        # split names and check length of list
        names = name.split()
        if len(names) != 2:
            raise ValueError("name must have form 'First Last', separated "
                             "by a space")
        # assign first/last names
        self.firstName = str(names[0])
        self.lastName = str(names[1])
        return

    def setDOB(self, DOB=""):
        """ Change the DOB of a Person.

        Args:
            DOB (str): The person's DOB in MM/DD/YYYY format

        """

        # split DOB and check length of monthDayYear list
        monthDayYear = DOB.split("/")
        if len(monthDayYear) != 3:
            raise ValueError("Please enter DOB in MM/DD/YYYY format")
        # try to assign birth month/day/year
        try:
            self.birthMonth = int(monthDayYear[0])
            self.birthDay = int(monthDayYear[1])
            self.birthYear = int(monthDayYear[2])
        except ValueError:
            raise ValueError("Could not parse DOB. Make sure it is given in "
                             "MM/DD/YYYY format, where MM, DD, and YYYY are "
                             "all integers")
        return

    def getName(self):
        """ Get the full name of a Person in string format.

        return:
            str: Person's name in First Last format

        """

        return f"{self.firstName} {self.lastName}"

    def getDOB(self):
        """ Get the DOB of a Person in MM/DD/YYYY format.

        return:
            str: Person's name in MM/DD/YYYY format

        """

        return f"{self.birthMonth}/{self.birthDay}/{self.birthYear}"

    def canVote(self):
        """ Check whether the Person is old enough to vote in the U.S.A.

        return:
            bool: True if older than 18, False otherwise

        """

        from datetime import datetime
        # get today's date using built-in datetime module
        todayDay = datetime.now().day
        todayMonth = datetime.now().month
        todayYear = datetime.now().year
        # check today's date against person's age
        if todayYear > self.birthYear + 18:
            return True
        elif todayYear == self.birthYear + 18 and todayMonth > self.birthMonth:
            return True
        elif todayYear == self.birthYear + 18 and \
             todayMonth == self.birthMonth and \
             todayDay >= self.birthDay:
            return True
        else:
            return False

    def readInputFromUser(self):
        name = input("Please enter the Person's first and last name, separated by a space: ")
        DOB = input("Please enter the Person's DOB in MM/DD/YYYY format: ")
        self.setName(name)
        self.setDOB(DOB)
        return
