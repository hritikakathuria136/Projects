using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class WelcomeToMenu : MonoBehaviour
{
    public void goToMenu()
    {
        SceneManager.LoadScene("Main_Menu");
    }
}
