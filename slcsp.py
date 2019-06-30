# Run with python slcsp.py
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


# Parse zipcode in zips.csv to get state and rate area
def get_state(zipcode):
    state = ''
    with open(ZIPS_CSV, 'r') as zipsfile:
        reader = csv.DictReader(zipsfile)
        for row in reader:
            if zipcode in row['zipcode']:
                state = row['state']
                rate_area = row['rate_area']
                break

    return state, rate_area


# Find list of relevant rates
def get_rates(state, rate_area):
    rates = []
    with open(PLANS_CSV, 'r') as plansfile:
        reader = csv.DictReader(plansfile)
        for row in reader:
            if METAL_LEVEL in row['metal_level']:
                if state in row['state'] and rate_area in row['rate_area']:
                    rates.append(row['rate'])

    return rates


# Get second smallest value in rates list
def get_second_lowest_value_in_list(rates):
    rates_set = set(rates)
    if len(rates_set) == 1:
        return sorted(rates_set)[0]
    elif len(rates_set) < 1:
        return ''
    else:
        return sorted(rates_set)[1]


def main():
    with open(SLCSP_COMPLETED_CSV, 'w') as target:
        writer = csv.writer(target)
        writer.writerow(['zipcode', 'rate'])

        zipcodes = get_zipcodes()
        for zipcode in zipcodes:
            state, rate_area = get_state(zipcode)
            rates = get_rates(state, rate_area)
            rate = get_second_lowest_value_in_list(rates)
            # print(zipcode + ', ' + rate)
            writer.writerow([zipcode, rate])


if __name__ == '__main__':
    main()
