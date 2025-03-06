#include "CareerCalculator.h"

CareerCalculator::CareerCalculator() {
}

using namespace std;

bool CareerCalculator::CalculateMaxCareer(const std::vector<int>& steps) {
    int maxReach = 0; // Initialize the maximum reachable index to 0
    int step = 0; // Initialize the current step to 0
    bool feasible = true; // Initialize the feasibility to true
    while (feasible && step < steps.size()) {
        if (step > maxReach) {
            // If the current index is greater than the maximum reachable index,
            // it means we cannot reach this position, so return false
            feasible = false;
        } else{
            // Update the maximum reachable index
        	maxReach = max(maxReach, step + steps[step]);
        	if (maxReach >= steps.size() - 1) {
            	// If the maximum reachable index is greater than or equal to the last index,
            	// it means we can reach or exceed the last position, so return true
            	feasible = true;
        	}
        }
        step++;
    }
    // If we finish the loop without reaching the last position, return false
    return feasible;
}