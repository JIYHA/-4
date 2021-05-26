for i in range(len(addresses)):
     if addresses[i][:4] == "www.":
        addresses[i] = "http://" + addresses[i]
    if not addresses[i][-4:] == ".com":
        addresses[i] = addresses[i] + ".com"