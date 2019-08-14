import auto_segmentation
import raw2train as training_preprocess
import training
import predict
import coordinate as coordinate_adjust
import output

input_video_name = "TestVideo"

# training data preprocessing input params
pre_dir = "./preprocessing/Data/training/data/"
raw_data = input_video_name
ext = ".csv"

# has players' position info? 1/0 : yes/no
# if yes, player_pos_file (.csv) is needed
player_pos_option = 0
player_pos_file = ''
# training with specific frames? 1/0 : yes/no
# if yes, specific_frame_file (.csv) is needed
frame_option = 0
specific_frame_file = ''

# unique_id for get_velocity function
unique_id = ''

preprocessed_filename = pre_dir + raw_data + "_preprocessed" + ext
raw_data = pre_dir + raw_data + ext

if player_pos_option != 0:
	player_pos_file += ext
if frame_option != 0:
	specific_frame_file += ext


# training and predict input params
result_dir = "./preprocessing/Data/training/result/"
model_path = "./preprocessing/Data/training/model/model.joblib.dat"

#name_train = "video3_train"
name_result = input_video_name+"_predict_result"

#filename_train = pre_dir + name_train + ext
filename_result = result_dir + name_result + ext

# segmentation filename
segmentation_path = "./preprocessing/Data/AccuracyResult/"
segmentation_input = ""
segmentation_output = "record_segmentation"

segmentation_input = segmentation_path + segmentation_input + ext
segmentation_output = segmentation_path + segmentation_output + ext

# output json file
json__ext = ".json"
rally_count_json_filename = input_video_name+"_rally_count_our_test"
rally_type_json_filename = ""
output_json_dir = "./preprocessing/Data/Output/"

rally_count_json_filename = output_json_dir + rally_count_json_filename + json__ext
rally_type_json_filename = output_json_dir + rally_type_json_filename + json__ext

if __name__ == "__main__":
    print("Content-Type: text/plain")    # plain is following
    print()                             # blank line, end of headers
    
    # Run segmentation
    auto_segmentation.begin()

	# training and prediction
    coordinate_adjust.run(segmentation_output, raw_data)
    training_preprocess.run(raw_data, preprocessed_filename, unique_id, player_pos_option, frame_option, player_pos_file, specific_frame_file)  #preprocess data
    #training.verify(pre_dir, filename_train, model_path)  #train model
    predict.verify(pre_dir, preprocessed_filename, model_path, result_dir, filename_result) #predict testing data

    # output json file
    #"../../Data/training/data/out.csv", "../../Data/training/result/0811_predict_result.csv", "../../Data/Output/rally_count_our.json", ""
    output.run(raw_data, filename_result, rally_count_json_filename, rally_type_json_filename)