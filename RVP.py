import streamlit as st
import numpy as np

# Function to calculate RVP blend
def calculate_rvp_blend(rvps, flow_rates):
    """
    Calculate the RVP of the blend using RVP blending indices.

    Parameters:
    rvps (list): List of RVP values for the components.
    flow_rates (list): Corresponding flow rates (in BPD) for the components.

    Returns:
    float: Blended RVP value.
    """
    # Calculate the RVP blending indices for each component
    rvp_indices = [rvp ** 1.25 for rvp in rvps]

    # Calculate the weighted RVP index
    weighted_rvp_index = sum(flow_rate * rvp_index for flow_rate, rvp_index in zip(flow_rates, rvp_indices))

    # Calculate the blended RVP
    blend_rvp = (weighted_rvp_index / sum(flow_rates)) ** (1 / 1.25)

    return blend_rvp

# Streamlit App
def app():
    st.title("Blending Calculations - RVP")

    # Inputs from the user
    st.sidebar.header("Enter Flow Rates and RVP values")
    
    flow_rates = []
    rvps = []
    
    num_components = st.sidebar.number_input("Number of components", min_value=1, step=1, value=4)
    
    for i in range(num_components):
        flow_rate = st.sidebar.number_input(f"Flow rate for component {i+1} (BPD)", min_value=1)
        rvp = st.sidebar.number_input(f"RVP for component {i+1} (psi)", min_value=0.0)
        
        flow_rates.append(flow_rate)
        rvps.append(rvp)

    # Perform calculation when button is pressed
    if st.sidebar.button("Calculate Blended RVP"):
        if len(flow_rates) > 0 and len(rvps) > 0:
            blended_rvp = calculate_rvp_blend(rvps, flow_rates)
            st.subheader(f"Blended RVP: {blended_rvp:.2f} psi")
        else:
            st.error("Please enter valid values for flow rates and RVP.")

if __name__ == "__main__":
    app()
