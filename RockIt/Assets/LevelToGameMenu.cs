using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelToGameMenu : MonoBehaviour
{
    public void goToMenuFetch()
    {
        SceneManager.LoadScene("Menu_Fetch it");
    }
}

