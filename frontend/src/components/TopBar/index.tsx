'use client'

import React, { useRef } from 'react'

import Link from 'next/link'
import Image from 'next/image'

import SearchIcon from './Icons/SearchIcon'
import XIcon from './Icons/XIcon'
import { usePathname } from 'next/navigation'
// import AccountDropdown from './AccountDropdown'
import { signOut, useSession } from 'next-auth/react'
import { useSearchContext } from '@/context/searchContext'


export default function TopBar(): React.ReactElement {
  const { data: session, status } = useSession()

  const pathname = usePathname()
  const ctx = useSearchContext()

  const handleInputFocus = () => ctx.setIsInputActive(true)
  const handleInputBlur = () => {
    if (ctx.searchInput === '') ctx.setIsInputActive(false)
  }
  const inputRefLg = useRef<HTMLInputElement>(null)
  const inputRefSm = useRef<HTMLInputElement>(null)



  return (
    <>
      <header className={`sticky top-0 flex flex-wrap lg:justify-start lg:flex-nowrap w-full bg-black text-sm py-[19.2px] border-b border-[#141414] px-[4%] z-[50] shadow-md shadow-[rgb(255,255,255,0.02)]`}>
        <nav
          className=' w-full mx-auto flex items-center justify-between'
          aria-label='Global'
        >
          <div className='flex items-center justify-between w-full'>
            <Link href='/' className='flex items-center cursor-pointer'>
              <div className='h-8 w-8 relative'>
                <Image
                  src='/logo.png'
                  alt='logo'
                  layout='fill'
                  objectFit='cover'
                  className=''
                />
              </div>
              <h3 className='ml-2 text-[30px] font-semibold leading-5 text-white font-fabada'>
                Brand
              </h3>
            </Link>

            <div className='pl-5 flex items-center w-full justify-between' >
              <Link
                href='/browse?sort=Trending'
                className={`transition duration-200 ${pathname === '/browse'
                  ? 'text-white font-semibold'
                  : 'text-[#e5e5e5] hover:text-[#979797]'
                  } translate-y-[6px]`}
              >
                Watch History
              </Link>

              <div className='hidden lg:flex items-center gap-x-4 text-white'>

                <div
                  className='relative group'
                  onClick={() => {
                    console.log('active')
                    if (inputRefLg.current) {
                      inputRefLg.current.focus()
                    }
                  }}
                >
                  <button className='group absolute peer left-[10px] top-2 peer cursor-default hover:cursor-pointer'>
                    <SearchIcon
                      strokeClasses={` group-focus:stroke-[#5848BC] ${ctx.isInputActive ? 'stroke-[#8414fb]' : 'stroke-[#dcdcdc]'
                        } transition duration-100`}
                    />
                  </button>
                  <input
                    ref={inputRefLg}
                    value={ctx.searchInput}
                    onChange={(e) => ctx.setSearchInput(e.target.value)}
                    onFocus={handleInputFocus}
                    onBlur={handleInputBlur}
                    className={`${ctx.isInputActive
                      ? 'w-[300px] cursor-auto bg-[#1E1E1E]'
                      : 'w-[44px] cursor-default bg-black'
                      } focus:cursor-auto peer py-auto h-[40px]  transition-all  duration-500 rounded-full border-none  pr-0 pl-[44px] text-[15px] font-light leading-6 text-[#979797] focus:ring-1 focus:ring-transparent`}
                    type='text'
                    placeholder='Sci-fi stories with hidden twists ...'
                    style={{ outline: 'none', resize: 'none' }}
                  />
                  <button
                    className={`absolute right-[10px] top-3 ${ctx.searchInput === '' ? 'hidden' : 'flex'
                      }`}
                    onClick={() => {
                      ctx.setSearchInput("")
                      ctx.setIsInputActive(false)
                    }}
                  >
                    <XIcon />
                  </button>
                </div>
                {/* {(status !== 'loading' && session) && <AccountDropdown />} */}
                {(status !== 'loading' && !session) && (
                  <div className='flex items-center gap-x-3 text-white font-semibold' >
                    <Link href='/login' className='text-[#e5e5e5] hover:text-[#979797]' >Login</Link>
                  </div>
                )}
                {status === "loading" && (
                  <div className='h-[40px] w-[40px] ' >&nbsp;</div>
                )}
              </div>
            </div>
          </div>
        </nav>
      </header>
    </>
  )
}

