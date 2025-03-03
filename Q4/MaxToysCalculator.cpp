// Marc Olivier Jean Paul: 20241763
// Abdelghafour Rahmouni: 20246224

#include "MaxToysCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe MaxToysCalculator
// this file contains the definitions of the methods of the MaxToysCalculator class

using namespace std;

MaxToysCalculator::MaxToysCalculator()
{
}

int MaxToysCalculator::CalculateMaxToys(const vector<int>& Toys, int S) { 
    // Pour deposer les jouets quand la somme dépensée est superieure à S
    int depot = 0; 
    // Longueur maximale de la séquence de jouets achetés à la suite
    int longeurMax = 0;
 
    // Parcourir tous les jouets
    for (int indexFin = 0; indexFin < Toys.size(); indexFin++) {
       // Quand on achète un jouet, on le retire de la somme totale
       S -= Toys[indexFin];
 
       // Tant que la somme totale est négative
       while (S < 0) {
          // On depose le jouet le plus ancien
          S += Toys[depot];
          depot++;
       }
 
       // Mettre à jour la longueur maximale
       longeurMax = max(longeurMax, indexFin - depot + 1);
    
    }
    
    // Retourner la longueur maximale
    return longeurMax;
 }
 
