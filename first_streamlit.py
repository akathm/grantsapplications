import streamlit as st
import pandas as pd

# Function to update the CSV file with the decision
def update_decision(data, row_index, decision):
    data.loc[row_index, 'Decision'] = decision
    data.to_csv('my_applications.csv', index=False)

# Function to display counts of accepted and rejected applications
def display_counts(data):
    accepted_count = len(data[data['Decision'] == 'Approve'])
    rejected_count = len(data[data['Decision'] == 'Reject'])
    st.write(f"Accepted: {accepted_count}")
    st.write(f"Rejected: {rejected_count}")

# Main function
def main():
    # Load the CSV file
    data = pd.read_csv('my_applications.csv')

    # Create review queue
    review_queue = data[data['Decision'].isnull()]

    # Display counts
    display_counts(data)

    # Iterate through the review queue
    for i, row in review_queue.iterrows():
        st.write(f"### Application #{i+1}")
        st.write(row)  # Display application details

        # Display links
        st.write("Links:")
        st.write(f"Twitter: {row['twitter']}")
        st.write(f"GitHub: {row['github']}")
        st.write(f"Grants Manager: {row['grants-manager']}")

        # Reviewer decision
        decision = st.radio("Decision", ('Approve', 'Reject'))

        # Update decision in CSV
        if st.button('Submit Decision'):
            update_decision(data, i, decision)
            st.success('Decision updated successfully.')
            st.write('---')
        else:
            st.warning('Please submit the decision before proceeding to the next entry.')
            break

# Run the app
if __name__ == '__main__':
    main()
