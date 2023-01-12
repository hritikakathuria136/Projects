using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Tutorial_Fetch : MonoBehaviour
{
    public void goToTutorial()
    {
        SceneManager.LoadScene("Tutorial_Fetch");
    }
}
