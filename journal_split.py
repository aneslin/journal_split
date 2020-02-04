from csv import DictReader, DictWriter

def eightFiftyTwoSplitter (row):
            working_row= row['"HOL852"']
            tag_split = working_row.split("$$")
            tag_split.pop(0)
            print(tag_split)
            dictList= {"b":'', "c":'',"k":'',"h":'',"i":'',"l":'', "m":'', "other":[]}
            for tag in tag_split:
                if tag[0] == "b":
                    dictList["b"] = tag[1:]
                elif tag[0] == "c":
                    dictList["c"] = tag[1:]
                elif tag[0] == "k":
                    dictList["k"] =tag[1:]
                elif tag[0] == "h":
                    dictList["h"] = tag[1:]
                elif tag[0] == "i":
                    dictList["i"]=tag[1:]
                elif tag[0] == "l":
                    dictList["l"]=tag[1:]
                elif tag[0] == "m":
                    dictList["m"] = tag[1:]
                else:
                    dictList["other"].append(tag[1:])
            return(dictList)


with open ("target.csv", 'w', newline='') as csvFile:
    fieldnames = ["SYSNO","TEXT_245","TEXT_130","TEXT_240","TEXT_022","TEXT_OCLC","TEXT_362","TEXT_OWN_AM",
                  "TEXT_TYP","HOL_SYS", "HOL_866",
                   "852_b", "852_c", "852_k", "852_h", "852_i", "852_l", "852_m",  "852_other"]
    writer = DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    with open ("Copy of amh_journal extract (002).csv", "r") as file:
        dictFile = DictReader(file)
        for row in dictFile:
            tag852 = eightFiftyTwoSplitter(row)
            writer.writerow({"SYSNO" : row['"SYSNO"'], 'TEXT_245':row['"TEXT_245"'], 'TEXT_130': row['"TEXT_130"'], 'TEXT_240': row['"TEXT_240"'],
                             'TEXT_022': row['"TEXT_022"'], 'TEXT_OCLC': row['"TEXT_OCLC"'], 'TEXT_362': row['"TEXT_362"'],
                             "TEXT_OWN_AM": row['"TEXT_OWN_AM"'], 'TEXT_TYP': row['"TEXT_TYP"'], "HOL_SYS": row['"HOL_SYS"'],
                             'HOL_866':row['"HOL_866"'],
                             "852_b": tag852["b"], "852_c": tag852["c"],
                             "852_k": tag852["k"], "852_h": tag852["h"],
                             "852_i": tag852["i"], "852_l":tag852["l"], "852_m":tag852["m"], "852_other":"; ".join(tag852["other"]) })







