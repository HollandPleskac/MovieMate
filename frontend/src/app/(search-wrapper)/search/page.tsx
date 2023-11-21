'use client'
// import Footer from '@/components/Footer'
import { ReadonlyURLSearchParams, useSearchParams } from 'next/navigation'
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import { useSearchContext } from '@/context/searchContext'

export default function Home() {
    const router = useRouter()
    const searchParams = useSearchParams()
    const ctx = useSearchContext()

    function getURLParams(searchParams: ReadonlyURLSearchParams): string {
        const newParams = new URLSearchParams(searchParams.toString());
        newParams.delete("q")
        return `?${newParams.toString()}`;
    }

    useEffect(() => {
        if (ctx.searchInput === '') {
            router.push(ctx.lastPage + getURLParams(searchParams))
        }
    }, [ctx.searchInput])

    return (
        <>
            <main className='w-full flex flex-col h-full'>
                DISPLAY SOME MOVIES MATCHING SEARCH HERE {ctx.searchInput}

            </main>
            {/* <Footer /> */}
        </>
    )
}
