using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Pause_Menu : MonoBehaviour
{
    public static bool GameIsPaused=false;
    public GameObject pauseMenuUI;


    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if(GameIsPaused)
            {
                Resume();
            }
            else
            {
                Pause();
            }
        }
    }

    public void Resume()
    {
        pauseMenuUI.SetActive(false);
        Time.timeScale=1;
        GameIsPaused=false;
    
    }

    public void Pause()
    {
        pauseMenuUI.SetActive(true);
        Time.timeScale=0;
        GameIsPaused=true;
    }

    public void LoadMenu()
    {
        SceneManager.LoadScene("Level_Menu");
        Time.timeScale=1;
    }

    public void QuitGame()
    {
        Debug.Log("The game has ended");
        Application.Quit();
    }
}
