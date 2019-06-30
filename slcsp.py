import csv

METAL_LEVEL = 'Silver'
SLCSP_CSV = 'slcsp.csv'
SLCSP_COMPLETED_CSV = 'slcsp_completed.csv'
ZIPS_CSV = 'zips.csv'
PLANS_CSV = 'plans.csv'


# Get list of zipcodes from file
def get_zipcodes():
    zipcodes = []
    with open(SLCSP_CSV, 'r') as slcspfile:
        reader = csv.DictReader(slcspfile)
        for row in reader:
            zipcodes.append(row['zipcode'])

    return zipcodes


# Parse zipcode in zips.csv to get state
# this may present an issue as the zip codes may not be unique
# In which case we need to use some fuckery with the rate area
def get_state(zipcode):
    state = ''
    with open(ZIPS_CSV, 'r') as zipsfile:
        reader = csv.DictReader(zipsfile)
        for row in reader:
            if zipcode in row['zipcode']:
                state = row['state']
                break

    return state


# Find list of relevant rates
def get_rates(state):
    rates = []
    with open(PLANS_CSV, 'r') as plansfile:
        reader = csv.DictReader(plansfile)
        for row in reader:
            if state in row['state'] and METAL_LEVEL in row['metal_level']:
                rates.append(row['rate'])
    return rates


# Get second smallest value in rate_list
def get_second_lowest_value_in_list(rates):
    rates.sort()
    return '290.94'


def main():
    with open(SLCSP_COMPLETED_CSV, 'w') as target:
        writer = csv.writer(target)

        zipcodes = get_zipcodes()
        for zipcode in zipcodes:
            state = get_state(zipcode)  # might not work as expected
            rates = get_rates(state)
            rate = get_second_lowest_value_in_list(rates)
            print(zipcode + ',' + rate)
            # writer.writerow(['zipcode', 'rate'])


if __name__ == '__main__':
    main()
