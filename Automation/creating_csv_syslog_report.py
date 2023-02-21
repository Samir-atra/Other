#!/usr/bin/env python3

import csv
import re


def get_dictionaries():
    typey = {}
    user = {}
    listy = []

    with open("syslog.log") as file:
        for entry in file:
            type_pattern = re.search(r"ticky: ERROR:? ([\w' ]*)", entry)
            user_pattern = re.search(r"(\([A-Za-z.0-9]*\))", entry)
            if type_pattern:
                beedoo = type_pattern.group(0).split()
                del beedoo[1]
                del beedoo[0]
                beed = ""
                for i in beedoo:
                    beed += i + " "
                if str(beed) not in typey.keys():
                    typey[beed] = 1
                else:
                    typey[beed] = int(typey.get(beed)) + 1

            if user_pattern:
                banana = user_pattern.group(0).strip(")(")
                if banana not in user.keys():
                    user[banana] = {"INFO": 0, "ERROR": 0}
                    if "ERROR" in entry:
                        user[banana] = {
                            "INFO": int(user[banana].get("INFO")),
                            "ERROR": int(user[banana].get("ERROR")) + 1,
                        }
                    elif "INFO" in entry:
                        user[banana] = {
                            "INFO": int(user[banana].get("INFO")) + 1,
                            "ERROR": int(user[banana].get("ERROR")),
                        }

                else:
                    if "ERROR" in entry:
                        user[banana] = {
                            "INFO": int(user[banana].get("INFO")),
                            "ERROR": int(user[banana].get("ERROR")) + 1,
                        }
                    elif "INFO" in entry:
                        user[banana] = {
                            "INFO": int(user[banana].get("INFO")) + 1,
                            "ERROR": int(user[banana].get("ERROR")),
                        }

        typey = sorted(typey.items(), key=lambda item: item[1], reverse=True)
        user_list = sorted(user.items(), key=lambda item: item[0])
        for iem in user_list:
            listy.append([iem[1]["INFO"], iem[1]["ERROR"]])
    return typey, user_list, listy


def gen_csv():
    types_list, users_list, listy = get_dictionaries()
    with open("error_message.csv", "a+") as err:
        field_names = ["Error", "Count"]
        writer = csv.writer(err)
        writer.writerow(field_names)
        for row in types_list:
            writer.writerow(row)

    with open("user_statistics.csv", "a+") as stats:
        fields = ["Username", "INFO", "ERROR"]
        writer = csv.writer(stats)
        writer.writerow(fields)
        counter = 0
        for r in users_list:
            x = [r[0], listy[counter][0], listy[counter][1]]
            writer.writerow(x)
            counter += 1


gen_csv()
