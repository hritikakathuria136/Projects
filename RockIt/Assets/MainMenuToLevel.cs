using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenuToLevel : MonoBehaviour
{
     public void goToLevel()
    {
        SceneManager.LoadScene("Level_Menu");
    }
}
