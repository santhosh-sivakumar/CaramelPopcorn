int search(int* nums, int numsSize, int value) {
    int mid, low = 0, high = numsSize - 1;

    while(low <= high)
    {
        mid = (low + high) / 2;

        if(nums[mid] == value)
            return mid;
        if(nums[mid] > value)
            high = mid - 1;
        if(nums[mid] < value)
            low = mid + 1;
    }

    return -1;
}