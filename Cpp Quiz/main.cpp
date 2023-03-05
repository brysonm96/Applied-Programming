#include <iostream>
#include <string>
using namespace std;

int playerScore;
int Guess;
 
//Question Class
class Question{

//Determines quiz item data types
private:
    string questionString;
    string firstAnswer;
    string secondAnswer;
    string thirdAnswer;
    string fourthAnswer;
    int correctAnswer;
    int correctScore;
public:
    void setValues(string, string,
                   string, string,
                   string, int);
 
    void askQuestion();
};
 
//Game
int main()
{
    cout << "-- MUSIC QUIZ --"
         << endl;
    cout << "This quiz covers various music topics"
         << endl;
    cout << "You need at least 70 points to pass"
         << endl;
    cout << "\n"
         << endl;
    cout << "Press Enter to start" << endl;
 
    cin.get();
 
    //Question class objects
    Question q1;
    Question q2;
    Question q3;
    Question q4;
    Question q5;
    Question q6;
    Question q7;
    Question q8;
    Question q9;
    Question q10;
    
    //Question, Guesses, Correct Answer
    q1.setValues("Which of the following is not a wind instrument?", 
                "Oboe", "Cello", "Clarient", "Bassoon", 2);
    q2.setValues("Who is the composer of Toccata and Fugue in D minor?", 
                "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Antonio Vivaldi", 1);
    q3.setValues("Around what time was the boroque music era?", 
                "1400-1550", "1780-1850", "1800-1870", "1600-1750", 4);
    q4.setValues("How many notes are in a C Major scale?", 
                "Five", "Six", "Three", "Eight", 4);
    q5.setValues("How many beats are in a Waltz meter?", 
                "Three", "One", "Five", "Two", 1);
    q6.setValues("How many strings does a traditional violin have?", 
                "Six", "Eight", "Four", "Five", 3);
    q7.setValues("What is the term for the speed that a musical piece is played?", 
                "Melody", "Dynamics", "Tempo", "Texture", 3);
    q8.setValues("What is a vocal musical piece unaccompanied by instruments called?", 
                "Symphony", "A Capella", "Chorus", "Concerto", 2);
    q9.setValues("What Century was the Piano invented in?", 
                "16th", "19th", "17th", "18th", 4);
    q10.setValues("Which of the following tempo speeds are the fastest?", 
                "Presto","Largo", "Adagio", "Allegro", 1);
 
    q1.askQuestion();
    q2.askQuestion();
    q3.askQuestion();
    q4.askQuestion();
    q5.askQuestion();
    q6.askQuestion();
    q7.askQuestion();
    q8.askQuestion();
    q9.askQuestion();
    q10.askQuestion();
 
    //Results
    cout << endl;
        cout << "\n" << endl;
        cout << "The quiz is finished!";
        cout << "\n" << endl;
 
    //User passed with an A
    if (playerScore > 89) {
        cout << "Congrats! You passed the quiz with an A!" << endl;
    }
    
    //User passed with a B
    else if (playerScore > 79 && playerScore < 90) {
        cout << "Good job! You passed the quiz with a B!" << endl;
    }
    
    //User passed with a C
    else if (playerScore > 69 && playerScore < 80) {
        cout << "Not bad! You passed the quiz with a C!" << endl;
    }
 
    //User did not pass
    else {
        cout << "You ended with a score of " << playerScore;
        cout << "." << endl;
        cout << "Sorry! You need at least a 70 to pass." << endl;
        cout << "Better luck next time." << endl;
    }
    return 0;
}
 
//Set question values

void Question::setValues(
    string question, string answer1,
    string answer2, string answer3,
    string answer4, int correct)
{
    questionString = question;
    firstAnswer = answer1;
    secondAnswer = answer2;
    thirdAnswer = answer3;
    fourthAnswer = answer4;
    correctAnswer = correct;
    correctScore = 10;
}
 
//Ask questions
void Question::askQuestion()
{
 
    //Show answer options
    cout << questionString << endl;
    cout << "1: " << firstAnswer << endl;
    cout << "2: " << secondAnswer << endl;
    cout << "3: " << thirdAnswer << endl;
    cout << "4: " << fourthAnswer << endl;
    cout << endl;
 
    cout << "Enter the corresponding number for your answer."
         << endl;
    cin >> Guess;
 
        //Correct answer response
    if (Guess == correctAnswer) {
        cout << endl;
        cout << "Correct!" << endl;
        playerScore = playerScore + correctScore;
        cout << "Your score is: " << playerScore;
        cout << "\n" << endl;
        
    }
 
        //Incorrect answer response
    else {
        cout << endl;
        cout << "Incorrect!" << endl;
        cout << "The correct answer was "
             << correctAnswer
             << "" << endl;
        cout << "Your score is: " << playerScore;
        cout << "\n" << endl;
    }
}
