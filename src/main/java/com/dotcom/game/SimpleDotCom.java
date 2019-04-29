package com.dotcom.game;



public class SimpleDotCom
{
    int[] locationCell ;
    int numberOfHit = 0;



    public void  setLocationCell(int[] locs)
    {
        locationCell = locs;
    }

    // prompt the user to enter guess number
    public String checkYourSelf(String userGuess)
    {
        int guess = Integer.parseInt(userGuess);

        String result = "miss";

        for (int cell : locationCell){

            if (guess == cell){
                result = "hit";

                numberOfHit ++;
                break;
            } // end if

        }// end for

        if (numberOfHit == locationCell.length)
        {
            result  = "kill";
        }// end if

        System.out.println(result);

        return result;


    }


}
