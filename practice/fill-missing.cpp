#include <iostream>
#include <vector>
#include <string>

// id: {1, 2, 3}, N: 7
// result: {1, 1, 1, 2, 2, 3, 3}
// time O(N), space O(N) 
std::vector<int> repeat_ids(std::vector<int> id, int N) {
  int n = id.size();
  if (N <= n) {
	return id;
  }
  
  int q = N / n; // q copies of each id
  int r = N % n; // r additional copies
  
  std::vector<int> result;
  for(int i = 0; i < n; ++i) {
	  
	for(int j = 0; j < q; ++j) {
	  result.push_back(id[i]);
	}
	
	if (r > 0) {
	  result.push_back(id[i]);
	  --r;
	}
  }
  return result;
}

// img_ty: {N, C, N}, img_id: {1, 2, 3}, N: 6
// result: {2, 1, 2, 1, 2, 3}
// time O(N), space O(N) 
std::vector<int> fill_missing(
      const std::string& img_ty, 
	  const std::vector<int>& img_id, int N) {

  // target length must be even
  if (N % 2 != 0) {
	return std::vector<int>();
  }
  
  // separate color IDs form nir IDs
  std::vector<int> col_id;
  std::vector<int> nir_id;
  for(int i = 0; i < img_ty.size(); ++i) {	  
	if (img_ty[i] == 'C') {
	  col_id.push_back(img_id[i]);
	} else if (img_ty[i] == 'N') {
	  nir_id.push_back(img_id[i]);
	}
  }
  
  // must have at least one color ID and one nir ID
  if (col_id.size() == 0 || nir_id.size() == 0) {
	return std::vector<int>();
  }
  
  // repeat ID "uniformly"
  col_id = repeat_ids(col_id, N/2);
  nir_id = repeat_ids(nir_id, N/2);
  
  // interleave color and nir IDs
  std::vector<int> result;
  for(int i = 0; i < N/2; ++i) {
	result.push_back(col_id[i]);
	result.push_back(nir_id[i]);
  }
  return result;
}


int main() {
  std::string img_ty;
  std::vector<int> img_id;
  int N;
  std::vector<int> result;
  
  while (std::cin >> img_ty) {
	img_id = std::vector<int>(img_ty.size());
	for(int i = 0; i < img_ty.size(); ++i) {
	  std::cin >> img_id[i];
	}
	std::cin >> N;

	result = fill_missing(img_ty, img_id, N);
	for(int i = 0; i < result.size(); ++i) {
	  std::cout << result[i] << ' ';
	}
	std::cout << std::endl;
  }
  return 0;
}
  
  
  
  
  
  