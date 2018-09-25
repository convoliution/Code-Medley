fn main() {
    let mut v: Vec<i32> = vec![7, 8, 3, 9, 5, 5, 1, 2, 6, 2];

    //print before sort
    println!("Unsorted:\n{:?}", v);

    let len = v.len();
    quicksort(&mut v, 0, len-1);

    //print after sort
    println!("Sorted:\n{:?}", v);
}

fn quicksort<T: Ord + Copy>(v: &mut Vec<T>, i_left: usize, i_right: usize) {
    if i_left < i_right {
        let i_pivot: usize = partition(v, i_left, i_right);
        quicksort(v, i_left, i_pivot);
        quicksort(v, i_pivot+1, i_right);
    }
}

// Hoare's partitioning method
fn partition<T: Ord + Copy>(v: &mut Vec<T>, mut i_left: usize, mut i_right: usize) -> usize {
    let val_pivot: T = v[i_left + (i_right - i_left)/2]; // val at middle index
    loop {
        while v[i_left] < val_pivot {
            i_left += 1;
        }
        while v[i_right] > val_pivot {
            i_right -= 1;
        }
        if i_left < i_right {
            v.swap(i_left, i_right);
            i_left += 1;
            i_right -= 1;
        } else {
            return i_right;
        }
    }
}
