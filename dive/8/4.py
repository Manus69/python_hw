import csv

def count_tot(ifile, ofile, fnames : list):
    tot = {}

    with open(ifile, "r") as _ifile:
        reader = csv.DictReader(_ifile)
        for row in reader:
            product = row[fnames[0]]
            quant = int(row[fnames[1]])
            price = float(row[fnames[2]])
            val = quant * price

            if product in tot: tot[product] += val
            else : tot[product] = val

    with open(ofile, "w") as _ofile:
        writer = csv.DictWriter(_ofile, [fnames[0], fnames[3]])
        writer.writeheader()

        for product, val in tot.items():
            writer.writerow({fnames[0] : product, fnames[3] : val})
