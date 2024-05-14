#include <stdio.h>

double interpolate(double array[], double x[], double xi, int n) {
    double result = 0;

    for (int i = 0; i < n; i++) {
        double term = array[i];

        for (int j = 0; j < n; j++) {
            if (j != i) {
                term = term * (xi - x[j]) / (x[i] - x[j]);
            }
        }

        result += term;
    }

    return result;
}
