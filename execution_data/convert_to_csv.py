import pickle
import csv

# Helper functions to extract data from different message types
def extract_pose_stamped(pose_stamped):
    position = pose_stamped.pose.position
    orientation = pose_stamped.pose.orientation
    return [position.x, position.y, position.z, orientation.w, orientation.x, orientation.y, orientation.z]

def extract_wrench(wrench):
    force = wrench.wrench.force
    torque = wrench.wrench.torque
    return [force.x, force.y, force.z, torque.x, torque.y, torque.z]

def extract_joint_states(joint_state):
    return list(joint_state)  # Assuming joint positions are most relevant, you can add velocity/effort if needed.

filename = 'data_trial5'

# Load the pickled dictionary from a file
with open(f'{filename}.pkl', 'rb') as file:
    data = pickle.load(file)

# Open a CSV file for writing
with open(f'{filename}.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Define the header based on the types of data you have
    header = [
        'current_pos_x', 'current_pos_y', 'current_pos_z', 'current_orientation_w', 'current_orientation_x', 'current_orientation_y', 'current_orientation_z',
        'goal_pos_x', 'goal_pos_y', 'goal_pos_z', 'goal_orientation_w', 'goal_orientation_x', 'goal_orientation_y', 'goal_orientation_z',
        'force_x', 'force_y', 'force_z', 'torque_x', 'torque_y', 'torque_z',
        'joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6', 'joint_7'  # Adjust based on the number of joints
    ]
    writer.writerow(header)
    
    # Now extract and write each row by unpacking the messages
    for i in range(len(data['pose'])):  # Assuming data has PoseStamped, Wrench, and JointStates
        curr_pose_data = extract_pose_stamped(data['pose'][i])
        goal_pose_data = extract_pose_stamped(data['goal'][i])
        wrench_data = extract_wrench(data['wrench'][i])
        joint_data = extract_joint_states(data['joint'][i])
        
        # Write the combined row
        row = curr_pose_data + goal_pose_data + wrench_data + joint_data
        writer.writerow(row)

print("Pickled ROS messages have been converted to CSV.")
