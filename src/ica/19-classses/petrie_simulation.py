class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee.
        """
        pass

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender
                + ": "
                + str(self.comments_received)
                + " sexist comments received")
