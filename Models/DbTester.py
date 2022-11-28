"""Tester file for DbHandler, make sure Models is pwd"""

import DbHandler


def main():
    """Main"""

    db_handler = DbHandler.DbHandler()

    info = {'name': "bambam", 'email': "ba@ba.m",
            'password': "qwerty", 'bio': ""}

    # db_handler.create_account(info)
    # db_handler.get_account(1)
    print(db_handler.email_exists("ba@ba.m"))
    print(db_handler.check_username_pw_match("bambam", "qwerty"))


if __name__ == "__main__":
    main()
