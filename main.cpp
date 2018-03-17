#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Sort non-decresing order
void ExchangeSort(int *data, int num_of_data) {
	for(int i = 0; i < num_of_data; ++i) {
		for(int j = i+1; j < num_of_data; ++j) {
			if (data[i] > data[j]) {
				int tmp = data[i];
				data[i] = data[j];
				data[j] = tmp;
			}
		}
	}
	return;
}

// Sort the non-decresing order
void MergeSort(int *data, int left, int right) {
	
	// Base case
	if(left == right) return;

	int mid = int((left + right) / 2);
	MergeSort(data, left, mid);
	MergeSort(data, mid+1, right);

	int* tmp = new int[right - left + 1];
	int left_ptr = left;
	int right_ptr = mid + 1;
	int tmp_ptr = 0;
	while(left_ptr <= mid || right_ptr <= right) {
		if(left_ptr > mid) {
			tmp[tmp_ptr] = data[right_ptr];
			right_ptr += 1;
		} else if(right_ptr > right) {
			tmp[tmp_ptr] = data[left_ptr];
			left_ptr += 1;
		} else if(data[left_ptr] < data[right_ptr]) {
			tmp[tmp_ptr] = data[left_ptr];
			left_ptr += 1;
		} else if(data[left_ptr] >= data[right_ptr]) {
			tmp[tmp_ptr] = data[right_ptr];
			right_ptr += 1;
		} else {
			cerr << "[!] Error in while loop" << endl;
			return;
		}
		tmp_ptr += 1;
	}

	for(int i = 0; i < right - left + 1; ++i) {
		data[left + i] = tmp[i];
	}

	delete[] tmp;
	return;
}

void InitData(int *data, int num_of_data) {
	
	for(int i = 0; i < num_of_data; ++i) {
		// range(1 ~ 1000)
		data[i] = rand() % 1000 + 1;
	}
	int num_of_print = (num_of_data > 10 ? 10 : num_of_data);
	cout << "Original data: " << endl;
	for(int i = 0; i < num_of_print; ++i) {
		cout << data[i] << " ";
	}
	cout << " ..." << endl;
}

double cpu_time () {
	return (double)clock() / (double)CLOCKS_PER_SEC;
}

int main() {
	// Set seed number.
	srand(7);

	int num_of_data = 10000;
	int num_of_print = (num_of_data > 10 ? 10 : num_of_data);
	int *data;
	data = new int[num_of_data];
	
	cout << "[Exchange sort]" << endl;
	InitData(data, num_of_data);
	double start_time = cpu_time();
	ExchangeSort(data, num_of_data);
	cout << "Elapsed time for Exchange sort: " << cpu_time() - start_time << endl;
	cout << "Sorted data: " << endl;
	for(int i = 0; i < num_of_print; ++i) {
		cout << data[i] << " ";
	}
	cout << " ..." << endl;

	cout << "\n[Merge sort]" << endl;
	InitData(data, num_of_data);
	start_time = cpu_time();
	MergeSort(data, 0, num_of_data-1);
	cout << "Elapsed time for Merge sort: " << cpu_time() - start_time << endl;
	cout << "Sorted data: " << endl;
	for(int i = 0; i < num_of_print; ++i) {
		cout << data[i] << " ";
	}
	cout << " ..." << endl;
	
	delete [] data;
	return 0;
}