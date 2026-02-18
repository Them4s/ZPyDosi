def aggregate_spectrum(arr, G):
    """
    Aggregates a 2D array by summing over bins of size 2^G along the columns.

    Parameters:
    - arr: 2D numpy array of shape (N, M)
    - G: Integer specifying the binning factor

    Returns:
    - aggregated_arr: 2D numpy array of shape (N, M // (2 ** G))
    """
    # Validate input array dimensions
    if arr.ndim != 2:
        raise ValueError("Input array must be 2-dimensional.")
    
    N, M = arr.shape
    bin_size = 2 ** G

    # Check if M is divisible by 2^G
    if M % bin_size != 0:
        raise ValueError(f"The number of columns M={M} must be divisible by 2^G={bin_size}.")

    new_M = M // bin_size

    # Reshape and sum over the bins
    reshaped_arr = arr.reshape(N, new_M, bin_size)
    aggregated_arr = reshaped_arr.sum(axis=2)

    return aggregated_arr