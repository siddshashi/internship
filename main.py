import csv
see = open(r"C:\Users\sidds\Downloads\Planxdeltadays.csv")

f = csv.reader(see)

ppa_7 = 0
ppa_30 = 0
psa_7 = 0
psa_30 = 0
psm_7 = 0
psm_30 = 0
ppm_7 = 0
ppm_30 = 0

for i in f:
  if i[1] != '':
    if i[0] == 'plan_premium_annual' and int(i[1]) <= 7:
      ppa_7 += int(i[2])
    if i[0] == 'plan_premium_annual' and int(i[1]) <= 30:
      ppa_30 += int(i[2])
    if i[0] == 'plan_starter_annual' and int(i[1]) <= 7:
      psa_7 += int(i[2])
    if i[0] == 'plan_starter_annual' and int(i[1]) <= 30:
      psa_30 += int(i[2])
    if i[0] == 'plan_starter_monthly' and int(i[1]) <= 7:
      psm_7 += int(i[2])
    if i[0] == 'plan_starter_monthly' and int(i[1]) <= 30:
      psm_30 += int(i[2])
    if i[0] == 'plan_premium_monthly' and int(i[1]) <= 7:
      ppm_7 += int(i[2])
    if i[0] == 'plan_premium_monthly' and int(i[1]) <= 30:
      ppm_30 += int(i[2])



ppa_7 = (ppa_7 / 212) * 100
print(ppa_7)
ppa_30 = (ppa_30 / 212) * 100
print(ppa_30)
psa_7 = (psa_7 / 150) * 100
print(psa_7)
psa_30 = (psa_30 / 150) * 100
print(psa_30)
psm_7 = (psm_7 / 116) * 100
print(psm_7)
psm_30 = (psm_30 / 116) * 100
print(psm_30)
ppm_7 = (ppm_7 / 109) * 100
print(ppm_7)
ppm_30 = (ppm_30 / 109) * 100
print(ppm_30)

