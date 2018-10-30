def dataParser(data):
    result = []

    name = "Name(first last):"
    email = "Email:"
    sex = "Sex(M/F):"
    teamID = "Team Name:"
    projectName = "Project Name:"
    projectStat = "Project status(C for complete,I for incomplete):"

    f_name = data.rfind(name)
    f_email = data.rfind(email)
    f_sex = data.rfind(sex)
    f_teamID = data.rfind(teamID)
    f_proName = data.rfind(projectName)
    f_proStat = data.rfind(projectStat)

    nLoc = f_name + len(name)
    emLoc = f_email + len(email) + 1
    sLoc = f_sex + len(sex)
    tLoc = f_teamID + len(teamID)
    pnLoc = f_proName + len(projectName)
    psLoc = f_proStat + len(projectStat)

    nm = data[nLoc:f_email]
    result.append(nm.strip())

    em = data[emLoc:f_sex]
    result.append(em.strip())

    se = data[sLoc:f_teamID]
    result.append(se.strip())

    td = data[tLoc:f_proName]
    result.append(td.strip())

    pn = data[pnLoc:f_proStat]
    result.append(pn.strip())

    ps = data[psLoc:]
    result.append(ps.strip())

    return result
