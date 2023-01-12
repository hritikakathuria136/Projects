using System;
using UnityEngine;
using System.Collections.Generic;
using UnityEngine.UI;
using TMPro;
using System.Xml.Schema;
using Unity.IO.LowLevel.Unsafe;
using JetBrains.Annotations;
using UnityEditor;

public class Spawn2 : MonoBehaviour
{
    public GameObject enemy;
    public GameObject confuse;
    public GameObject fingers;
    public List<GameObject> entities = new List<GameObject>();
    public int enemyCount;
    public int confusingCount;
    public FingersUp fingerses;

    // countdown
    private float timeForCountdown = 3;
    private float timeBeforeCountdown = 3;
    private bool hasCountedDown = false;

    // scoring
    string[] medalNames = new string[] { "None :(", "Bronze", "Silver", "Gold" };
    int[] medalValues = new int[] { 0, 1, 3, 5 };
    public Text scoreText;
    public int score;
    int highScore;
    int lastTotalScore;
    int currentMedalIndex;
    int intermediateScore;

    [SerializeField] public TMP_Text amountText;
    [SerializeField] public TMP_Text resultText;
    [SerializeField] public TMP_Text counterText;

    void Start()
    {
        InvokeRepeating("Spawner", 1.0f, 11.0f);
        InvokeRepeating("Timer", 11.0f, 11.0f);
        InvokeRepeating("Game", 6.0f, 11.0f);
        InvokeRepeating("CleanText", 11.0f, 11.0f);

        score = 0;
        currentMedalIndex = 0;
        highScore = PlayerPrefs.GetInt("highscoreFingers");
        lastTotalScore = PlayerPrefs.GetInt("totalScore");

        scoreText.text = @"Highscore: " + highScore.ToString() + "\nPoints Collected: " + score.ToString() +
                        "\nCurrent Medal: " + medalNames[currentMedalIndex] + "\n" + intermediateScore.ToString() + " / " +
                        medalValues[currentMedalIndex + 1] + " for " + medalNames[currentMedalIndex + 1];
    }

    private void Update()
    {
        if (!hasCountedDown)
        {
            if (timeBeforeCountdown > 0)
            {
                timeBeforeCountdown -= Time.deltaTime;
            }
            else
            {
                Countdown();
            }
        }

        for(int i = 0; i< entities.Count; i++)
        {
            
            int dir = UnityEngine.Random.Range(1, 4);
            if (dir == 1) { entities[i].transform.Translate(0,-0.2f, 0); }                                             // Move 
            else if (dir == 2){ entities[i].transform.Translate(0, -0.2f, 0); }
            else if(dir == 3) { entities[i].transform.Translate(0.2f,0 , 0); }
            else { entities[i].transform.Translate(0.2f, 0, 0); } 

            }

  



    }

    void Timer()
    {
        foreach (GameObject u in entities)
        {
            Destroy(u);
        }
        entities.Clear();
    }

    void Spawner()
    {
        enemyCount = UnityEngine.Random.Range(1, 5);
        for (int i = 1; i <= enemyCount; i++)
        {
            // Correctly rotated enemies  (way up)  
            entities.Add(Instantiate(enemy, new Vector2(UnityEngine.Random.Range(0, Screen.width), UnityEngine.Random.Range(0, Screen.height))
                , Quaternion.identity));
            
        }

        confusingCount = UnityEngine.Random.Range(1, 10);
        for (int i = 0; i <= confusingCount; i++)
        {
            // Objects rotated differently
            entities.Add(Instantiate(confuse, new Vector2(UnityEngine.Random.Range(0, Screen.width), UnityEngine.Random.Range(0, Screen.height)),
                 Quaternion.Euler(180f, 180f, 0f)));
        }
        hasCountedDown = false;

    }

    public void Game()
    {
        int total = fingerses.GetComponent<FingersUp>().getTotal();
        // int total = fingers.getTotal();
        amountText.text = total.ToString();
        counterText.text = "";

        if (total == enemyCount)
        {
            resultText.text = "Correct!";
            score += 1;
            intermediateScore += 1;
            UpdateTotalScore();

            if (score > highScore)
            {
                UpdateHighScore();
            }

            if (currentMedalIndex != 3)
            {
                if (intermediateScore == medalValues[currentMedalIndex + 1])
                {
                    if (currentMedalIndex != 3)
                    {
                        currentMedalIndex += 1;
                        intermediateScore = 0;
                    }
                }
                scoreText.text = @"Highscore: " + highScore.ToString() + "\nPoints Collected: " + score.ToString() +
                        "\nCurrent Medal: " + medalNames[currentMedalIndex] + "\n" + intermediateScore.ToString() + " / " +
                        medalValues[currentMedalIndex + 1] + " for " + medalNames[currentMedalIndex + 1];

            }
            else
            {
                scoreText.text = @"Highscore: " + highScore.ToString() + "\nPoints Collected: " + score.ToString() +
                        "\nCurrent Medal: " + medalNames[currentMedalIndex] + "\nGood Job! You earned the highest medal :)";
            }
        }

        else
        {
            resultText.text = "Wrong!";
        }

        hasCountedDown = true;
        timeForCountdown = 3;
        timeBeforeCountdown = 2;

    }

    public void CleanText()
    {
        amountText.text = "";
        resultText.text = "";
        counterText.text = "";
    }

    public void Countdown()
    {
        if (timeForCountdown > 0)
        {
            timeForCountdown -= Time.deltaTime;
            counterText.text = (Math.Ceiling(timeForCountdown)).ToString() + "...";
        }

    }

    void UpdateHighScore()
    {
        highScore = score;
        PlayerPrefs.SetInt("highscoreFingers", lastTotalScore + score);
        PlayerPrefs.Save();
    }

    void UpdateTotalScore()
    {
        PlayerPrefs.SetInt("totalScore", lastTotalScore + score);
        PlayerPrefs.Save();
    }


}
