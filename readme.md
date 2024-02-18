# QuadReal IIIIIIIIII
group IIIIIIIIII's brainstorming page

I suggest each of us using our own dictionary, so that we can organize our work.
Please add a dictionary with your name as soon as you clone this, and push that.

# blake's idea
## about data
Three csv are provided.
1. devices.csv -> alias the device to the buildings ["device_id","building_id"]
2. reading_types.csv -> alias `value_type_id` to `reading_type_name` ["reading_type_id","reading_type_name"]
3. sampled_readings.csv -> ["device_id","date","value_type_id","value"]
4. test.csv -> ["device_id","date","value_type","value"(unknown)] ==>> fill "value"

## possible deductions -- need help!!
S1 devices in the same building should have similar values
