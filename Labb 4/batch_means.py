
#Categorizes CSV file. Each batch[0] contains their coordinates[1:3] and measurement[3].
def categorize_to_batches(csv_file):

    batches_sorted = {}

    with open(csv_file, 'r') as h:
        for line in h:
            four_values = line.split(',')
            batch = four_values[0]

            if not batch in batches_sorted:
                batches_sorted[batch] = []
            batches_sorted[batch] += [(four_values[1:])]

        return batches_sorted

#Calculates the average of measurements for each batch for coordinates within scope
def calculating_average_measurement(sorted_data):

    average_measurement_batch = {}

    for batch, coordinates_measurement in sorted_data.items():
        if len(coordinates_measurement) > 0:
            acceptable_batches = 0
            sum_of_measurements = 0


            for (coordinate1, coordinate2, measurement) in coordinates_measurement:
#Errorhandling in case of wrong input
                try:
                    if float(coordinate1)**2 + float(coordinate2)**2 <= 1:
                        sum_of_measurements += float(measurement)
                        acceptable_batches += 1

                except ValueError:
                    print("Something went wrong with the input for batch", batch,
                          "\nPlease look it over as results may be faulty.")


#errorhandling incase of division of zero.
            try:
                average_measurement = sum_of_measurements/acceptable_batches
                average_measurement_batch[batch] = average_measurement
            except ZeroDivisionError:
                print("All coordinates for batch", batch ,"were not accepted. Please look over your input.")

        else:
           average_measurement_batch[batch] = None

    return average_measurement_batch


#Presents the batch results. Moved it, since calculations and presentation of results
#should NOT be in the same function. For it to be resuable.
def batch_result(batch_result):
#short dictionary comprehension after sorting.
    sorted_keys = sorted(batch_result.keys())
    sorted_result = {key: batch_result[key] for key in sorted_keys}

    for batch, average in sorted_result.items():
        print(batch, "\t", average)


#Input of CSV file. Goes over each function until the result is given.
def main():
    try:
        data_file = input('Which data file? ')
        categorized = categorize_to_batches(data_file)
        average_batch = calculating_average_measurement(categorized)
        batch_result(average_batch)
    except FileNotFoundError:
        print("Could not find file. Please try again.")


#Starts program
if __name__ == '__main__':
    main()
