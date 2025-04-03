using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public Vector3 leftMoveForce;
    public Vector3 rightMoveForce;
    public float airDrag;
    public int jumpForce;
    public int zero;
    public float maxSpeedR;
    public float maxSpeedL;
    public Vector3 resetX;
    public Vector3 resetY;
    public Vector3 leftJump;
    public Vector3 rightJump;

    public int playerFacing;
    public bool canJump;
    public bool doubleJump;
    public bool wallJumpL;
    public bool wallJumpR;
    public float djTimer;
    void Start()
    {
        playerFacing = 1;
        resetY = GetComponent<Rigidbody2D>().linearVelocity;
        djTimer = 0;
        zero = 0;
        airDrag = 0.125f;
        maxSpeedR = 3f;
        maxSpeedL = maxSpeedR * -1;


    }

    void Update()
    {
        
        
        if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow))
        {
            playerFacing = 1;
            GetComponent<Rigidbody2D>().AddForce(rightMoveForce);
            if (GetComponent<Rigidbody2D>().linearVelocityX >= maxSpeedR)
            {
                GetComponent<Rigidbody2D>().linearVelocityX = maxSpeedR;
            }
        }

        if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow))
        {
            playerFacing = -1;
            GetComponent<Rigidbody2D>().AddForce(leftMoveForce);
            if (GetComponent<Rigidbody2D>().linearVelocityX <= maxSpeedL)
            {
                GetComponent<Rigidbody2D>().linearVelocityX = maxSpeedL;
            }
        }

        if (Input.GetKeyDown(KeyCode.W) || Input.GetKeyDown(KeyCode.UpArrow))
        {
            djTimer += Time.deltaTime;
            if (canJump == true)
            {
                canJump = false;
                GetComponent<Rigidbody2D>().linearVelocityY = jumpForce;
                doubleJump = true;
            }
            else if (doubleJump == true)
            {
                doubleJump = false;
                GetComponent<Rigidbody2D>().linearVelocityY = zero;
                GetComponent<Rigidbody2D>().linearVelocityY = jumpForce;
            }
            else if(wallJumpL == true)
            {
                wallJumpL = false;
                GetComponent<Rigidbody2D>().linearVelocity = resetX;
                GetComponent<Rigidbody2D>().linearVelocity = leftJump;
                doubleJump = true;
            }
            else if (wallJumpR == true)
            {
                wallJumpR = false;
                GetComponent<Rigidbody2D>().linearVelocity = resetX;
                GetComponent<Rigidbody2D>().linearVelocity = rightJump;
                doubleJump = true;
            }
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "Ground")
        {
            canJump = true;
            doubleJump = false;
            wallJumpR = false;
            wallJumpL = false;
        }

        if (collision.gameObject.tag != "Ground")
        {
            GetComponent<Rigidbody2D>().linearVelocityX -= airDrag;
        }

            if (collision.gameObject.tag == "Ceiling")
        {
            canJump = false;
        }

        if (collision.gameObject.tag == "WallL")
        {
            canJump = false;
            doubleJump = false;
            wallJumpL = true;
        }

        if (collision.gameObject.tag == "WallR")
        {
            canJump = false;
            doubleJump = false;
            wallJumpR = true;
        }
    }
}
