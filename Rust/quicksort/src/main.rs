extern crate rand;

use rand::distributions::{Range, IndependentSample};

// sort a randomly generated vector
fn main() {
    let between = Range::new(-9, 10);
    let mut rng = rand::thread_rng();

    let len: usize = 10;
    let mut v: Vec<i32> = Vec::new();
    for _ in 0..len {
        v.push(between.ind_sample(&mut rng));
    }

    //print before sort
    println!("Unsorted:\n{:?}", v);

    quicksort(&mut v, 0, len-1);

    //print after sort
    println!("Sorted:\n{:?}", v);
}

// Hoare's partitioning method
fn partition(v: &mut Vec<i32>, mut i_left: usize, mut i_right: usize) -> usize {
    let val_pivot: i32 = v[i_left + (i_right - i_left)/2]; // median index
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

fn quicksort(v: &mut Vec<i32>, i_left: usize, i_right: usize) {
    if i_left < i_right {
        let i_pivot: usize = partition(v, i_left, i_right);
        quicksort(v, i_left, i_pivot);
        quicksort(v, i_pivot+1, i_right);
    }
}
